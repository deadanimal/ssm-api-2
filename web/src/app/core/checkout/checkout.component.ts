import { Component, OnInit, TemplateRef } from '@angular/core';
import {
  FormGroup,
  FormBuilder,
  Validators,
  FormControl,
} from '@angular/forms';
import swal from 'sweetalert2';
import { Router } from '@angular/router';
import { BsModalRef, BsModalService } from 'ngx-bootstrap';

import { LoadingBarService } from '@ngx-loading-bar/core';

import { ProductCartsService } from 'src/app/shared/services/product-carts/product-carts.service';
import { ProductCart } from 'src/app/shared/services/product-carts/product-carts.model';

export enum SelectionType {
  single = 'single',
  multi = 'multi',
  multiClick = 'multiClick',
  cell = 'cell',
  checkbox = 'checkbox',
}

@Component({
  selector: 'app-checkout',
  templateUrl: './checkout.component.html',
  styleUrls: ['./checkout.component.scss'],
})
export class CheckoutComponent implements OnInit {
  
  // Modal
  modal: BsModalRef;
  modalConfig = {
    keyboard: true,
    class: 'modal-dialog-centered',
  };

  // Table
  tableEntries: number = 5;
  tableSelected: any[] = [];
  tableTemp = [];
  tableActiveRow: any;
  tableRows: any[] = [];
  SelectionType = SelectionType;

  // Form
  searchForm: FormGroup;
  searchField: FormGroup;
  addAppReqForm: FormGroup;
  editAppReqForm: FormGroup;

  // Data
  items: ProductCart[] = [];

  // Icons
  iconEmpty = 'assets/img/default/shopping-bag.svg';

  // declare variable
  sum: number = 0;
  total: number = 0;
  totaldocument: number = 0;

  // Checker
  isEmpty: boolean = false;

  constructor(
    private fb: FormBuilder,
    private loadingBar: LoadingBarService,
    private cartService: ProductCartsService,
    private modalService: BsModalService,
    private formBuilder: FormBuilder,
    private router: Router,
  ) {}

  ngOnInit(): void {
    this.getData()
  }

  getData() {
    this.cartService.getAll().subscribe(
      () => {
        this.items = this.cartService.ProductCarts
        this.tableRows = this.items
        console.log(this.tableRows)
      },
      () => {},
      () => {
        this.tableTemp = this.tableRows.map((prop, key) => {
          return {
            ...prop,
            id_index: key+1
          }
        })
      }
    )
  }

  removeItem(id: string) {
    this.cartService.delete(id).subscribe(
      () => {},
      () => {},
      () => {
        this.getData()
      }
    )
  }

  successAlert(task) {
    swal.fire({
      title: 'Success',
      text: task,
      icon: 'success',
      // showCancelButton: true,
      buttonsStyling: false,
      confirmButtonText: 'Close',
      customClass: {
        cancelButton: 'btn btn-outline-success',
        confirmButton: 'btn btn-success ',
      },
    });
    console.log('confirm');
  }

  makePayment() {
    this.loadingBar.start();
    this.loadingBar.complete();
  }

  remove() {
    console.log('Item removed');
  }

  navigatePage(path: string) {
    // console.log('Path: ', path)
    this.router.navigate([path]);
  }

  openModal(modalRef: TemplateRef<any>, row) {
    if (row) {
      console.log(row);
      this.editAppReqForm.patchValue(row);
    }
    this.modal = this.modalService.show(
      modalRef,
      Object.assign({}, { class: 'gray modal-lg' })
    );
    // this.modal = this.modalService.show(modalRef, this.modalConfig);
  }

  closeModal() {
    this.modal.hide();
    this.editAppReqForm.reset();
  }

  entriesChange($event) {
    this.tableEntries = $event.target.value;
  }

  filterTable($event) {
    let val = $event.target.value;
    this.tableTemp = this.tableRows.filter(function (d) {
      for (var key in d) {
        if (d[key].toLowerCase().indexOf(val) !== -1) {
          return true;
        }
      }
      return false;
    });
  }

  onSelect({ selected }) {
    this.tableSelected.splice(0, this.tableSelected.length);
    this.tableSelected.push(...selected);
  }

  onActivate(event) {
    this.tableActiveRow = event.row;
  }

}
