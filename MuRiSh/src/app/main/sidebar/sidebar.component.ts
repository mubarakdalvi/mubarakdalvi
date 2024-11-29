import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-sidebar',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './sidebar.component.html',
  styleUrl: './sidebar.component.css',
})
export class SidebarComponent {
  name = 'Whatisname'; //interplotion
  age = 15;
  is_male = true;
  bg_group = 'O';
  isbtndisabled = false;
  // two way data binding
  inputval1 = '';
  // two way binding with ngmodel
  inputval2 = '';
  // event binding
  onChange() {
    console.log('Hi');
  }
  // two way binding with event and property binding and interpolation
  myChange(e: Event) {
    const value = (e.target as HTMLInputElement).value;
    console.log(value);
  }
  // two way binding with ngmodel
  yourChange(e: Event) {
    const value = (e.target as HTMLInputElement).value;
    this.inputval1 = value;
  }
  ourChange(e: Event) {
    const value = (e.target as HTMLInputElement).value;
    this.inputval2 = value;
  }
}
