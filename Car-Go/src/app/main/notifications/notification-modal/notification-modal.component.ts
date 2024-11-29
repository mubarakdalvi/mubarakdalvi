import { Component, OnInit, EventEmitter, Input, Output } from '@angular/core';

@Component({
    selector: 'app-notification-modal',
    templateUrl: './notification-modal.component.html',
    styleUrl: './notification-modal.component.css',
    standalone: false
})
export class NotificationModalComponent implements OnInit {
  @Input() isVisible = false;
  @Output() closeNotification = new EventEmitter<void>();

  isNotificationtoggle = false;

  constructor() {}
  ngOnInit(): void {}

  notificationToggle(): void {
    this.isNotificationtoggle = !this.isNotificationtoggle;
  }

  closeToggle(): void {
    this.isVisible = false;
    this.closeNotification.emit();
  }
}
