import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AlertAndNotificatonsRoutingModule } from './alert-and-notificatons-routing.module';
import { AlertAndNotificatonsComponent } from './alert-and-notificatons.component';
import { FuelLevelWarningsComponent } from './fuel-level-warnings/fuel-level-warnings.component';
import { InsuarenceRegisterationRenewalReminderComponent } from './insuarence-registeration-renewal-reminder/insuarence-registeration-renewal-reminder.component';
import { MaintenanceReminderComponent } from './maintenance-reminder/maintenance-reminder.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AlertAndNotificatonsComponent,
    FuelLevelWarningsComponent,
    InsuarenceRegisterationRenewalReminderComponent,
    MaintenanceReminderComponent,
  ],
  imports: [
    CommonModule,
    AlertAndNotificatonsRoutingModule,
    FormsModule,
    ReactiveFormsModule,
  ],
  exports: [AlertAndNotificatonsComponent],
})
export class AlertAndNotificatonsModule {}
