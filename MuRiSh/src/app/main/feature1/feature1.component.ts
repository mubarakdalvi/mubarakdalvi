import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-feature1',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './feature1.component.html',
  styleUrl: './feature1.component.css',
})
export class Feature1Component {
  //with intepolation and control flow @for @if we can
  users = [
    { id: 1, name: 'git', isMale: true, age: 71 },
    { id: 2, name: 'rit', isMale: false, age: 1771 },
    { id: 3, name: 'jit', isMale: true, age: 40 },
    { id: 4, name: 'pit', isMale: false, age: 371 },
    { id: 5, name: 'mit', isMale: false, age: 171 },
    { id: 6, name: 'nit', isMale: false, age: 671 },
    { id: 7, name: 'pit', isMale: false, age: 971 }
  ];
}
