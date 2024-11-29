import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Router } from '@angular/router';

@Component({
    selector: 'app-navbar',
    templateUrl: './navbar.component.html',
    styleUrl: './navbar.component.css',
    standalone: false
})
export class NavbarComponent {
  @Input() isSidebarVisible = false;
  @Input() isSidebarToggle = false;
  @Output() closeSidebar = new EventEmitter<void>();
  @Output() hideSidebar = new EventEmitter<void>();

  constructor(private router: Router) {}

  close(): void {
    this.isSidebarToggle = !this.isSidebarToggle;
    this.closeSidebar.emit();
  }

  checkSidebar(): void {
    this.isSidebarVisible = !this.isSidebarVisible;
    this.hideSidebar.emit();
  }
}
