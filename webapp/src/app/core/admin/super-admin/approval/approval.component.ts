import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-approval',
  templateUrl: './approval.component.html',
  styleUrls: ['./approval.component.scss']
})
export class ApprovalComponent implements OnInit {

  // Image 
  imgConstruction = 'assets/img/default/under-construction.png'
  
  constructor() { }

  ngOnInit() {
  }

}
