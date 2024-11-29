import {
  AfterViewInit,
  booleanAttribute,
  Component,
  ElementRef,
  EventEmitter,
  Input,
  numberAttribute,
  OnChanges,
  OnDestroy,
  OnInit,
  Output,
  SimpleChanges,
  ViewChild,
} from '@angular/core';

@Component({
  selector: 'app-about',
  standalone: true,
  imports: [],
  templateUrl: './about.component.html',
  styleUrl: './about.component.css',
})
export class AboutComponent
  implements OnInit, OnDestroy, OnChanges, AfterViewInit
{
  // if we add implement and forget to load interface then implement will give error as we have implemented the interface but not used it yet

  @Input({ transform: numberAttribute }) id!: number;
  @Input({}) name = '';
  // @Input({ transform: booleanAttribute }) isMale!: boolean;
  @Input({ transform: numberAttribute }) age!: number;

  @Output() myEvent = new EventEmitter<{
    id: number;
    name: string;
    newAge: number;
  }>();
  sendData() {
    this.myEvent.emit({
      id: this.id,
      name: this.name,
      newAge: 1457,
    });
  }

  @ViewChild('mytitle') title?: ElementRef;

  // when file is running contructor first run
  constructor() {
    // initilization the property
    // depemdcy injection
    // event listner register
    // automatically called one time , and just one time when class instace is created
    console.log('Constructor called', this.name);
    console.log(
      'Constructor called',
      (this.title?.nativeElement.textContent)
    );
  }

  ngAfterViewInit(): void {
    console.log('AfterViewInit', this.title?.nativeElement.textContent);
  }

  // then it will run
  // it can run multiple times
  ngOnChanges(changes: SimpleChanges): void {
    console.log('ngonchanges', changes);
    console.log('ngonchanges', this.title?.nativeElement.textContent);
  }

  // then this will run
  ngOnInit() {
    //same thing canbe done but dependency injection cannot be done
    // initilization the property
    // event listner register
    // initial api call
    console.log('ngOnInit Called', this.name);
    console.log('ngOnInit Called', this.title?.nativeElement.textContent);
  }

  // then this will run unlike construtor and ngoninit it will run only one time
  ngOnDestroy() {
    console.log('Users Cleared');
  }
}


