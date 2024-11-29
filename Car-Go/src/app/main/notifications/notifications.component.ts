import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
@Component({
    selector: 'app-notifications',
    templateUrl: './notifications.component.html',
    styleUrl: './notifications.component.css',
    standalone: false
})
export class NotificationsComponent {
  notificationCount: number = 0;
  messageCount: number = 0;

  isNotificationVisible = false;

  isToggleVisible(): void {
    this.isNotificationVisible = !this.isNotificationVisible;
  }

  alertCounter() {}
}
