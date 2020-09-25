import { Component, OnInit } from "@angular/core";
import { Router } from "@angular/router";
import swal from "sweetalert2";
import {
  FormGroup,
  FormBuilder,
  Validators,
  FormControl,
} from "@angular/forms";

import { TransactionsService } from "src/app/shared/services/transactions/transactions.service";
import { AuthService } from "src/app/shared/services/auth/auth.service";
import { UsersService } from "src/app/shared/services/users/users.service";
import { IpService } from 'src/app/shared/services/ip/ip.service';
import { Ip } from 'src/app/shared/services/ip/ip.model';

import { tap } from "rxjs/operators";
import * as sjcl from 'sjcl';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import * as sha from 'js-sha256'

@Component({
  selector: "app-payment",
  templateUrl: "./payment.component.html",
  styleUrls: ["./payment.component.scss"],
})
export class PaymentComponent implements OnInit {
  
  // get data from auth service
  egovPackage: string;
  userType: string;
  userID: string;
  showIcondiv = false;
  userdetails: any;
  userPackage: string;
  clientIP: Ip

  // Form
  newBillingForm: FormGroup;
  transactionForm: FormGroup

  constructor(
    private router: Router,
    private TransactionsService: TransactionsService,
    private formBuilder: FormBuilder,
    private AuthService: AuthService,
    private IpService: IpService,
    private UsersService: UsersService,
    private http: HttpClient
  ) {
    this.userType = this.AuthService.userType;
    this.userID = this.AuthService.userID;
  }

  ngOnInit(): void {
    this.UsersService.getOne(this.userID).subscribe((res) => {
      this.userdetails = res;
      this.userPackage = this.userdetails.egov_package;
      console.log("this.egovPackage -> ", this.userPackage);
      console.log("this.userType -> ", this.userType);
      console.log("this.userID -> ", this.userID);
      this.egovPackage = this.userdetails.egov_package;
      if (this.userdetails.user_type == "EG") {
        this.showIcondiv == false;
      }

      console.log("data = ", this.userdetails.user_type);
      // console.log("Svc: ", this.tableRows);
    });

    this.newBillingForm = this.formBuilder.group({
      // id: new FormControl(""),
      name: new FormControl("", Validators.required),
      payment_method: new FormControl('DD', Validators.required),
      amount: new FormControl('', Validators.required)
    });

    this.transactionForm = this.formBuilder.group({
      TransactionType: new FormControl('SALE', Validators.required),
      PymtMethod: new FormControl('', Validators.required),
      ServiceID: new FormControl('', Validators.required),
      PaymentID: new FormControl('', Validators.required),
      OrderNumber: new FormControl('', Validators.required),
      PaymentDesc: new FormControl('', Validators.required),
      MerchantName: new FormControl('', Validators.required),
      MerchantReturnURL: new FormControl('', Validators.required),
      MerchantCallbackURL: new FormControl('', Validators.required),
      Amount: new FormControl('', Validators.required),
      CurrencyCode: new FormControl('MYR', Validators.required),
      CustIP: new FormControl('', Validators.required),
      CustName: new FormControl('', Validators.required),
      CustEmail: new FormControl('', Validators.required),
      CustPhone: new FormControl('', Validators.required),
      HashValue: new FormControl(Validators.required),
      MerchantTermsURL: new FormControl('http://merchA.merchdomain.com/terms.html', Validators.required),
      LanguageCode: new FormControl('en', Validators.required),
      PageTimeout: new FormControl('780', Validators.required),
    })

    this.clientIP = this.getClientIP()
  }

  addNewBillingData() {
    console.log("payment data -> ", this.newBillingForm);
    this.TransactionsService.create(this.newBillingForm.value).subscribe(
      (res) => {
        console.log(res);
        // this.successAlert("Successfully Save Data");
      },
      (err) => {
        console.log(err);
        // this.loadingBar.complete();
        // this.errorMessage();
        // console.log("HTTP Error", err), this.errorMessage();
      },
      () => console.log("HTTP request completed.")
    );
  }

  navigatePage(path: string) {
    // console.log('Path: ', path)
    this.router.navigate([path]);
  }

  makePayment() {
    swal
      .fire({
        title: "Confirmation",
        text: "Payment successfully been made!",
        icon: "info",
        buttonsStyling: false,
        confirmButtonText: "Okay",
        customClass: {
          confirmButton: "btn btn-primary ",
        },
      })
      .then((result) => {
        // if (result.value) {
        //   this.router.navigate(["/orders"]);
        // }
        this.addNewBillingData();
      });
    console.log("confirm");
    // this.tryMakePayment()
  }

  successAlert(task) {
    swal
      .fire({
        title: "Success",
        text: task,
        icon: "success",
        // showCancelButton: true,
        buttonsStyling: false,
        confirmButtonText: "Close",
        customClass: {
          cancelButton: "btn btn-outline-success",
          confirmButton: "btn btn-success ",
        },
      })
      .then((result) => {
        // console.log("confirm");
        window.location.reload();
        // this.navigatePage("/egov-details");
      });
  }

  calculateAmount() {
    console.log('Amount calculated')
  }

  tryMakePayment() {
    console.log('Payment made')
    this.transactionForm.controls['PymtMethod'].setValue('ANY')
    this.transactionForm.controls['ServiceID'].setValue('SM2')
    this.transactionForm.controls['PaymentID'].setValue('ajfka14891')
    this.transactionForm.controls['OrderNumber'].setValue('ODD124123')
    this.transactionForm.controls['PaymentDesc'].setValue('Testing 1 2 3')
    this.transactionForm.controls['MerchantCallbackURL'].setValue('https://portal.ssm.prototype.com.my//#/payment')
    this.transactionForm.controls['Amount'].setValue('100')
    this.transactionForm.controls['CustName'].setValue('Yusliadi')
    this.transactionForm.controls['CustIP'].setValue('1.1.1.1')
    this.transactionForm.controls['CustEmail'].setValue('test@prototype.com.my')
    this.transactionForm.controls['CustPhone'].setValue('0192846541')
    this.transactionForm.controls['HashValue'].setValue(this.hashTheShit())
    this.transactionForm.controls['MerchantTermsURL'].setValue('https://portal.ssm.prototype.com.my/#/terms-conditions')

    this.pay().subscribe()
  }


  pay() {
    let serviceUrl = 'https://test2pay.ghl.com/IPGSG/Payment.aspx'
    const headers = new HttpHeaders();
    headers.set('Content-Type', 'application/x-www-form-urlencoded')
    headers.set('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    return this.http.post<any>(serviceUrl, this.transactionForm.value, {headers: headers}).pipe(
      tap(
        (res) => {
        console.log("Payment", res);
        },
        (err) => {
          console.log(err)
        }
      )
    );
  }

  getClientIP(): any {
    this.IpService.get().subscribe(
      () => {
        this.clientIP = this.IpService.ip
      }
    )
  }

  hashTheShit() {
    let merchantPwd = 'sm212345'
    let merchantID = 'SM2'
    let paymentID = 'ajfka14891'
    let merchantReturnURL = 'https://portal.ssm.prototype.com.my/#/terms-conditions'
    let amount = '100'
    let currencyCode = 'MYR'
    let custIP = '1.1.1.1'
    let pageTimeout = '780'
    // Password + ServiceID + PaymentID + MerchantReturnURL + MerchantApprovalURL + MerchantUnApprovalURL + MerchantCallBackURL + Amount + CurrencyCode + CustIP + PageTimeout + CardNo + Token
    let valueToHash = merchantPwd+merchantID+paymentID+merchantReturnURL+amount+currencyCode+custIP+pageTimeout
    console.log('val', sha.sha256(valueToHash))
    return sha.sha256(valueToHash)
  }

}
