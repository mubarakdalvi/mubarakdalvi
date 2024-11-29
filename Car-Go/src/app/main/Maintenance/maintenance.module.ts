import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MaintenanceRoutingModule } from './maintenance-routing.module';
import { MaintenanceComponent } from './maintenance.component';
import { VehicleMaintenanceComponent } from './vehicle-maintenance/vehicle-maintenance.component';
import { MaintenanceHistoryComponent } from './maintenance-history/maintenance-history.component';

@NgModule({
  declarations: [
    MaintenanceComponent,
    VehicleMaintenanceComponent,
    MaintenanceHistoryComponent,
  ],
  imports: [CommonModule, MaintenanceRoutingModule],
  exports: [MaintenanceComponent],
})
export class MaintenanceModule {}
