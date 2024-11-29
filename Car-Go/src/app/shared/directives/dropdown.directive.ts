import {
  Directive,
  ElementRef,
  HostListener,
  Input,
  Renderer2,
} from '@angular/core';

@Directive({
    selector: '[appDropdown]',
    exportAs: 'appDropdown',
    standalone: false
})
export class DropdownDirective {
  @Input('appDropdown') dropDown!: HTMLElement;
  isOpen = false;

  constructor(private el: ElementRef, private renderer: Renderer2) {}

  @HostListener('document:click', ['$event'])
  toggleDropdown(event: Event): void {
    const clickInside = this.el.nativeElement.contains(event.target);
    if (clickInside) {
      this.isOpen = !this.isOpen;
    } else {
      this.isOpen = false;
    }
    this.setDropdownState();
  }

  private setDropdownState(): void {
    const dropdownMenu = this.el.nativeElement.querySelector('.dropDownMenu');
    if (this.isOpen) {
      this.renderer.addClass(dropdownMenu, 'block');
      this.renderer.removeClass(dropdownMenu, 'hidden');
    } else {
      this.renderer.addClass(dropdownMenu, 'hidden');
      this.renderer.removeClass(dropdownMenu, 'block');
    }
  }
}
