import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Router } from '@angular/router';

@Component({
    selector: 'app-sidebar',
    templateUrl: './sidebar.component.html',
    styleUrl: './sidebar.component.css',
    standalone: false
})
export class SidebarComponent {
  @Input() isSidebarVisible = false;
  @Input() isSidebarToggle = false;

  constructor(private router: Router) {}

  ngOnInit() {}
}
