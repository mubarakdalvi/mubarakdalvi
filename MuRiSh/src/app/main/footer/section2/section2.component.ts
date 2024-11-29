import { Component, EventEmitter, input, Output } from '@angular/core';
import { CounterService } from '../../../services/counter.service';

@Component({
  selector: 'app-section2',
  standalone: true,
  imports: [],
  providers: [CounterService],
  templateUrl: './section2.component.html',
  styleUrl: './section2.component.css',
})
export class Section2Component {
  constructor(public counterservice: CounterService) {}

  name = input("" ,{  //input signal intiialize with '' string datatype or any other
alias:'userName', // you can also add alias and transform
  })


@Output () ourEvent = new EventEmitter<string>()
sendData() {
this.ourEvent.emit(this.name()) // so
  console.log(this.name())
}
}
