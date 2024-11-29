import { NgModule, NO_ERRORS_SCHEMA } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PermissionsRoutingModule } from './permissions-routing.module';
import { PermissionsComponent } from '../permissions/permissions.component';
import { ManagePermissionComponent } from './manage-permission/manage-permission.component';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';

@NgModule({
  declarations: [PermissionsComponent, ManagePermissionComponent],
  imports: [
    CommonModule,
    PermissionsRoutingModule,
    CommonModule,
  ],
  exports: [PermissionsComponent],
})
export class PermissionsModule {}
