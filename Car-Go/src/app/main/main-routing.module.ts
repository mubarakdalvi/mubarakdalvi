import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MainComponent } from './main.component';
import { DashboardComponent } from './dashboard/dashboard.component';

const routes: Routes = [
  {
    path: '',
    component: MainComponent,
    children: [
      {
        path: '',
        redirectTo: 'dashboard',
        pathMatch: 'full',
      },
      {
        path: 'dashboard',
        component: DashboardComponent,
      },
      {
        path: 'accounts',
        loadChildren: () =>
          import('./accounts/accounts.module').then(
            (mod) => mod.AccountsModule
          ),
      },
      {
        path: 'maintenance',
        loadChildren: () =>
          import('./Maintenance/maintenance.module').then(
            (mod) => mod.MaintenanceModule
          ),
      },
      {
        path: 'additional-features',
        loadChildren: () =>
          import('./additional-features/additional-features.module').then(
            (mod) => mod.AdditionalFeaturesModule
          ),
      },
      {
        path: 'alert-and-notificatons',
        loadChildren: () =>
          import('./alert-and-notificatons/alert-and-notificatons.module').then(
            (mod) => mod.AlertAndNotificatonsModule
          ),
      },
      {
        path: 'authentication',
        loadChildren: () =>
          import('./authentication/authentication.module').then(
            (mod) => mod.AuthenticationModule
          ),
      },
      {
        path: 'expense-tracker',
        loadChildren: () =>
          import('./expense-tracker/expense-tracker.module').then(
            (mod) => mod.ExpenseTrackerModule
          ),
      },
      {
        path: 'fuel-record',
        loadChildren: () =>
          import('./fuel-record/fuel-record.module').then(
            (mod) => mod.FuelRecordModule
          ),
      },
      {
        path: 'insurance-management',
        loadChildren: () =>
          import('./insurance-management/insurance-management.module').then(
            (mod) => mod.InsuranceManagementModule
          ),
      },
      {
        path: 'notification',
        loadChildren: () =>
          import('./notifications/notification.module').then(
            (mod) => mod.NotificationModule
          ),
      },
      {
        path: 'permissions',
        loadChildren: () =>
          import('./permissions/permissions.module').then(
            (mod) => mod.PermissionsModule
          ),
      },
      {
        path: 'report-and-analytics',
        loadChildren: () =>
          import('./report-and-analytics/report-and-analytics.module').then(
            (mod) => mod.ReportAndAnalyticsModule
          ),
      },
      {
        path: 'service-record',
        loadChildren: () =>
          import('./service-record/service-record.module').then(
            (mod) => mod.ServiceRecordModule
          ),
      },
      {
        path: 'staff-management',
        loadChildren: () =>
          import('./staff-management/staff-management.module').then(
            (mod) => mod.StaffManagementModule
          ),
      },
      {
        path: 'store-document',
        loadChildren: () =>
          import('./store-documents/store-document.module').then(
            (mod) => mod.StoreDocumentModule
          ),
      },
      {
        path: 'vehicle-management',
        loadChildren: () =>
          import('./vehicle-management/vehicle-management.module').then(
            (mod) => mod.VehicleManagementModule
          ),
      },
    ],
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class MainRoutingModule {}
