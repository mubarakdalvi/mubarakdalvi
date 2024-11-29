import { computed, effect, Injectable, Signal, signal } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class CounterService {
  private count = 0; //we will create getter and setter method

  getCounter() {
    return this.count; // for accessing the count variable in amy compoenent we have to use this getter method
  }

  increamentCounter() {
    this.count = this.count + 1;
  }

  decreamentCounter() {
    this.count = this.count - 1;
  }

  private sig = signal(0); //we are creating signal with default initial value

  // here we have created computed signal,
  doublesig: Signal<number> = computed(() => this.sig() * 2);
  // we will use getter setter method here also

  constructor(){
    effect(() => {
      console.log(`signal value : ${this.sig()} Double Count ${this.doublesig()}`) //for debuging purpose only
    })
  }

  getsig() {
    return this.sig();
  }

  increamentSig() {
    // this.sig.set(5); // we will use set method to directly pass the value, otherwise we will give as
    this.sig.set(this.sig()+1);  // or we can use this update on previous value
    // this.sig.update((oldval) =>{
    //   return oldval + 1; // with this we can also update the value,
    // })
  }
}
