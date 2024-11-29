import { Component } from '@angular/core';
import { FaqsComponent } from '../faqs/faqs.component';
import { AboutComponent } from '../about/about.component';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ContainerComponent } from '../container/container.component';
import { Feature1Component } from "../../feature1/feature1.component";
import { Section1Component } from "../section1/section1.component";
import { Section2Component } from "../section2/section2.component";

@Component({
  selector: 'app-footer',
  standalone: true,
  imports: [FaqsComponent, AboutComponent, CommonModule, FormsModule, ContainerComponent, Feature1Component, Section1Component, Section2Component],
  templateUrl: './footer.component.html',
  styleUrl: './footer.component.css',
})
export class FooterComponent {
  users = [
    { id: 1, name: 'git', isMale: true, age: 71 },
    { id: 2, name: 'rit', isMale: false, age: 1771 },
    { id: 3, name: 'jit', isMale: true, age: 40 },
    { id: 4, name: 'kit', isMale: false, age: 371 },
    { id: 5, name: 'mit', isMale: false, age: 171 },
    { id: 6, name: 'nit', isMale: false, age: 671 },
    { id: 7, name: 'pit', isMale: false, age: 971 },
  ];

  recievedData(myData: { id: number; name: string; newAge: number }) {
    console.log(myData)
    const userIndex1 = this.users.findIndex((user) => user.name == myData.name);
    this.users[userIndex1].age = myData.newAge;
  }

  clear() {
    this.users = [];
  }
}
