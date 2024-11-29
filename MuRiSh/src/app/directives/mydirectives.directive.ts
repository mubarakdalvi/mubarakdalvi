import { Directive, ElementRef, HostBinding, HostListener } from '@angular/core';

@Directive({
  selector: '[appMydirectives]',
  standalone: true,
})
export class MydirectivesDirective {

  constructor(public el: ElementRef) { // dependy injection
  }

  @HostBinding('style.border')
  border = '1px solid tomato';

  @HostListener('mouseenter')
  changeFontSize() {
    console.log('Mouse Entered');
    this.el.nativeElement.style.fontSize = '21px';
  }

  @HostListener('mouseleave')
  resetFontSize() {
    console.log('Mouse Leave');
    this.el.nativeElement.style.fontSize = '18px'
  }
}
