import { AfterViewInit, Component, OnInit } from '@angular/core';
import { MyservicesService } from '../../../services/myservices.service';
import e from 'express';

@Component({
  selector: 'app-container',
  standalone: true,
  imports: [],
  templateUrl: './container.component.html',
  styleUrl: './container.component.css',
})
export class ContainerComponent implements OnInit, AfterViewInit {
  constructor(private myjoke: MyservicesService) {}
  // ngOnInit() {
  //   this.myjoke.getservice().subscribe((data: any) => {
  //     this.joke = data.value; // if we cannot access data directly then we can give value to variable
  //   });
  // }

  ngOnInit(): void {
    this.getAnotherJoke();
  }

  getAnotherJoke() {
    //with this method we are getting another joke
    this.myjoke.getservice().subscribe((data: any) => {
      this.joke = data.value; // with this method if we cannot access data directly then we can give value to variable
    }, (err) => {
      console.log('Error Found',err);
    }
  );
  }

  ngAfterViewInit(): void {}

  joke = 'loading';
}
