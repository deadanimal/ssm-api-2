import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-product-management',
  templateUrl: './product-management.component.html',
  styleUrls: ['./product-management.component.scss']
})
export class ProductManagementComponent implements OnInit {

  // Image 
  imgConstruction = 'assets/img/default/under-construction.png'
  
  constructor() { }

  ngOnInit() {
  }

}
