import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { StaffManagementRoutingModule } from './staff-management-routing.module';
import { StaffManagementComponent } from '../staff-management/staff-management.component';
import { AssignVehicleWorkComponent } from './assign-vehicle-work/assign-vehicle-work.component';
import { StaffWorkingTimeComponent } from './staff-working-time/staff-working-time.component';
import { MonitorPerformanceComponent } from './monitor-performance/monitor-performance.component';

@NgModule({
  declarations: [
    StaffManagementComponent,
    AssignVehicleWorkComponent,
    StaffWorkingTimeComponent,
    MonitorPerformanceComponent,
  ],
  imports: [CommonModule, StaffManagementRoutingModule],
  exports: [StaffManagementComponent],
})
export class StaffManagementModule {}
