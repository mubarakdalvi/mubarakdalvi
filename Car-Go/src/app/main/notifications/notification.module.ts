import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { NotificationRoutingModule } from './notification-routing.module';
import { NotificationSettingsComponent } from './notification-settings/notification-settings.component';
import { NotificationsComponent } from './notifications.component';
import { NotificationModalComponent } from './notification-modal/notification-modal.component';
import { MessageComponent } from '../notifications/message/message.component';
import { MessageModalComponent } from '../notifications/message/message-modal/message-modal.component';

@NgModule({
  declarations: [
    NotificationsComponent,
    NotificationSettingsComponent,
    NotificationModalComponent,
    MessageComponent,
    MessageModalComponent,
  ],
  imports: [CommonModule, NotificationRoutingModule],
  exports: [NotificationsComponent],
})
export class NotificationModule {}
