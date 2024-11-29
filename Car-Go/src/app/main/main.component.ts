import { Component, Input } from '@angular/core';

@Component({
    selector: 'app-main',
    templateUrl: './main.component.html',
    styleUrl: './main.component.css',
    standalone: false
})
export class MainComponent {
  isSidebarVisible: boolean = false;
  isSidebarToggle: boolean = false;

  toggleSidebar(): void {
    this.isSidebarToggle = !this.isSidebarToggle;
  }

  isSidebar(): void {
    this.isSidebarVisible = !this.isSidebarVisible;
  }
}
