import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AlertAndNotificatonsComponent } from './alert-and-notificatons.component';
import { FuelLevelWarningsComponent } from './fuel-level-warnings/fuel-level-warnings.component';
import { InsuarenceRegisterationRenewalReminderComponent } from './insuarence-registeration-renewal-reminder/insuarence-registeration-renewal-reminder.component';
import { MaintenanceComponent } from '../../main/Maintenance/maintenance.component';

const routes: Routes = [
  {
    path: '',
    component: AlertAndNotificatonsComponent,
    children: [
      {
        path: 'fuel-and-notification',
        component: FuelLevelWarningsComponent,
      },
      {
        path: 'insuarence-registeration-renewal-reminder',
        component: InsuarenceRegisterationRenewalReminderComponent,
      },
      {
        path: 'maintenance-reminder',
        component: MaintenanceComponent,
      },
    ],
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AlertAndNotificatonsRoutingModule { }
