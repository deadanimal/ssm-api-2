import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-usages',
  templateUrl: './usages.component.html',
  styleUrls: ['./usages.component.scss']
})
export class UsagesComponent implements OnInit {

  // Image 
  imgConstruction = 'assets/img/default/under-construction.png'
  
  constructor() { }

  ngOnInit() {
  }

}
