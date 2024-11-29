import { AfterViewInit, Component, ElementRef, ViewChild } from '@angular/core';
import { CounterService } from '../../../services/counter.service';

@Component({
  selector: 'app-section1',
  standalone: true,
  imports: [],
  providers: [CounterService], // with this we are createing difference instance for different compoenent
  templateUrl: './section1.component.html',
  styleUrl: './section1.component.css',
})
export class Section1Component {
  @ViewChild('buttonEffect') btneffect?: ElementRef;
  constructor(public counterservice: CounterService) {
    // we use contructor for injecting dependencies
    // getCount(){
    //   return this.counterservice.getCounter()
    // }
  }
  // this cahnges the code , and not the responsiveness when hover
  // ngAfterViewInit(): void {
  //   if (this.btneffect) {
  //     this.btneffect.nativeElement.style.fontSize = '10px';
  //   } else {
  //     console.error('Button element not found!');
  //   }
  // }

}
