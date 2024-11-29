import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProfileRoutingModule } from './accounts-routing.module';
import { AccountsComponent } from './accounts.component';
import { ProfileManagementComponent } from './profile-management/profile-management.component';
import { ChangePasswordComponent } from './change-password/change-password.component';
import { LogoutComponent } from './logout/logout.component';
import { SharedModule } from '../../shared/shared.module';
import { ContactusComponent } from './contact-us/contact-us.component';

@NgModule({
  declarations: [
    AccountsComponent,
    ChangePasswordComponent,
    ProfileManagementComponent,
    LogoutComponent,
    ContactusComponent

  ],
  imports: [CommonModule, ProfileRoutingModule, SharedModule],
  exports: [AccountsComponent],
})
export class AccountsModule {}
