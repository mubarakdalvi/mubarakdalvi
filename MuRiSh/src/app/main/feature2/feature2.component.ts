import { CommonModule } from '@angular/common';
import { booleanAttribute, Component, Input, numberAttribute, Output ,EventEmitter} from '@angular/core'; // component is also decorator and also input is decorator
import { FormsModule } from '@angular/forms';
import { User } from '../../../model/user';

// import { EventEmitter } from 'node:stream'; // please make sure to import correct event emmiter as we have emmiter in node module also that will not work

//we cannt make function in between compoent and ecport classs
// or here we can make  functions
// function formatname(value:string){
//   return "Hey " + value;
// }

@Component({
  selector: 'app-feature2',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './feature2.component.html',
  styleUrl: './feature2.component.css',
})
// cannot make function here cause it will give error in class export name
export class Feature2Component {
  // we can make funcion here
  // we are passing parent to child data
  // these attributes convertt string to value povided with the correct data type attribute
  @Input({ transform: numberAttribute }) id!: number;
  // @Input({ alias: 'userName', transform: formatname }) name = ''; // with this we can give other name to same function and using custome function name formatname which we are applying by using transformation method
  @Input({ alias: 'userName' }) name = ''; // here using without transformation
  @Input({ transform: booleanAttribute }) isMale!: boolean; // values are not initialize means we have not provided the variable a value like in above we have provided name = ''
  @Input({ transform: numberAttribute }) age!: number; // have to provide boolean attribute and number attribute so when giving value as a strig it will not give us eroor
  // now we are passing data from child to parent
  @Output() myEvent = new EventEmitter<string>();
  sendData1() {
    this.myEvent.emit('Hey');
  }
  // now we are updating with output decorator from child to parent with same method but few changes
  @Output() ourEvent = new EventEmitter<{
    id: number;
    name: string;
    newAge: number;
  }>(); //here we have created an object ad without type or interface file creation
  sendData2() {
    this.ourEvent.emit({ id: this.id, name: this.name, newAge: 1541 });
    // also here we are intiating object which we have created
    // we are hardcoding value her to get updated when
    // user click on button 2 then age will get updated to 1541
  }
  @Output() yourEvent = new EventEmitter<User>(); //here we will import the type file or interface file which have created with name of user.ts inside model folder
  sendData3() {
    this.yourEvent.emit({ id: this.id, name: this.name, newAge: 2024 });
    // also here we are intiating object which we have created the this.name is from input decorator
    // we are hardcoding value her to get updated when
    // user click on button 3 then age will get updated to 2024
  }
}


