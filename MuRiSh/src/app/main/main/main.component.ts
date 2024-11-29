import { Component } from '@angular/core';
import { SidebarComponent } from "../sidebar/sidebar.component";
import { Feature1Component } from '../feature1/feature1.component';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Feature2Component } from "../feature2/feature2.component";
import { User } from '../../../model/user';

@Component({
  selector: 'app-main',
  standalone: true,
  imports: [
    SidebarComponent,
    Feature1Component,
    CommonModule,
    FormsModule,
    Feature2Component,
  ],
  templateUrl: './main.component.html',
  styleUrl: './main.component.css',
})
export class MainComponent {
  // now we are doing parent to child data
  // looping with directive and output decorator with that parent to child data showing

  users = [
    { id: 1, name: 'git', isMale: true, age: 71 },
    { id: 2, name: 'rit', isMale: false, age: 1771 },
    { id: 3, name: 'jit', isMale: true, age: 40 },
    { id: 4, name: 'pit', isMale: false, age: 371 },
    { id: 5, name: 'mit', isMale: false, age: 171 },
    { id: 6, name: 'nit', isMale: false, age: 671 },
    { id: 7, name: 'pit', isMale: false, age: 971 },
  ];
  recievedData1(s: string) {
    console.log(s);
  }
  // we cannot any other variable name here we have stricly to add same name provided in child component
  recievedData2(myData :{id:number, name:string, newAge:number}) { //here we have to create a container for
    console.log(myData); // like we have created an object here and in that we have our variables wwe can do it with another way in that we have to create an interface or type file,that we have created

    const userIndex1 =  this.users.findIndex(user=>user.name == myData.name )
    this.users[userIndex1].age = myData.newAge
  }
  recievedData3(u:User) {
    console.log(u);
    const userIndex2 = this.users.findIndex(user=>user.name == u.name)
    this.users[userIndex2].age = u.newAge;
  }
}
