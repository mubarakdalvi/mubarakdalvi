import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderRoutingModule } from './header-routing.module';
import { ProfileComponent } from '../profile/profile.component';
import { FormsModule } from '@angular/forms';
import { HeaderComponent } from './header.component';
import { RolePermissionsComponent } from './roles/role-permissions/role-permissions.component';
import { SharedModule } from '../../shared/shared.module';

@NgModule({
  declarations: [ProfileComponent, HeaderComponent],
  imports: [CommonModule, HeaderRoutingModule, FormsModule],
  exports: [HeaderComponent,ProfileComponent]
})
export class HeaderModule {}
