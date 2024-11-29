import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MainRoutingModule } from './main-routing.module';
import { AllVehicleComponent } from './all-vehicle/all-vehicle.component';
import { ReadyToGoVehiclesComponent } from './ready-to-go-vehicles/ready-to-go-vehicles.component';
import { AppSettingsComponent } from './app-settings/app-settings.component';
import { TutorialsComponent } from './tutorials/tutorials.component';
import { SidebarComponent } from './layout/sidebar/sidebar.component';
import { AuthenticationModule } from './authentication/authentication.module';
import { ExpenseTrackerModule } from './expense-tracker/expense-tracker.module';
import { FuelRecordModule } from './fuel-record/fuel-record.module';
import { InsuranceManagementModule } from './insurance-management/insurance-management.module';
import { MaintenanceModule } from './Maintenance/maintenance.module';
import { PermissionsModule } from './permissions/permissions.module';
import { ReportAndAnalyticsModule } from './report-and-analytics/report-and-analytics.module';
import { ServiceRecordModule } from './service-record/service-record.module';
import { StaffManagementModule } from './staff-management/staff-management.module';
import { StoreDocumentModule } from './store-documents/store-document.module';
import { VehicleManagementModule } from './vehicle-management/vehicle-management.module';
import { DashboardComponent } from './dashboard/dashboard.component';
import { AdditionalFeaturesModule } from './additional-features/additional-features.module';
import { AlertAndNotificatonsModule } from './alert-and-notificatons/alert-and-notificatons.module';
import { RecentActivityComponent } from './recent-activity/recent-activity.component';
import { AccountsModule } from './accounts/accounts.module';
import { NavbarComponent } from './layout/navbar/navbar.component';
import { SharedModule } from '../shared/shared.module';
import { FooterComponent } from './layout/footer/footer.component';
import { NotificationModule } from './notifications/notification.module';
import { HelpComponent } from './layout/footer/help/help.component';
import { SupportComponent } from './layout/footer/support/support.component';
import { NavbarModule } from './layout/navbar/navbar.module';
import { RouterModule } from '@angular/router';
import { MatIconModule } from '@angular/material/icon';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AllVehicleComponent,
    ReadyToGoVehiclesComponent,
    AppSettingsComponent,
    TutorialsComponent,
    SidebarComponent,
    DashboardComponent,
    RecentActivityComponent,
    NavbarComponent,
    FooterComponent,
    SupportComponent,
    HelpComponent,
  ],
  imports: [
    CommonModule,
    MainRoutingModule,
    AuthenticationModule,
    ExpenseTrackerModule,
    FuelRecordModule,
    InsuranceManagementModule,
    MaintenanceModule,
    PermissionsModule,
    ReportAndAnalyticsModule,
    ServiceRecordModule,
    StaffManagementModule,
    StoreDocumentModule,
    VehicleManagementModule,
    AdditionalFeaturesModule,
    AlertAndNotificatonsModule,
    AccountsModule,
    SharedModule,
    NotificationModule,
    NavbarModule,
    RouterModule,
    MatIconModule,
    ReactiveFormsModule,
    FormsModule,
  ],
  exports: [NavbarComponent, SidebarComponent, FooterComponent],
})
export class MainModule {}
