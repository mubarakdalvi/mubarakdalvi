import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FuelRecordRoutingModule } from './fuel-record-routing.module';
import { TrackFuelConsumptionComponent } from './track-fuel-consumption/track-fuel-consumption.component';
import { FuelRecordComponent } from '../fuel-record/fuel-record.component';
import { FuelEfficiencyComponent } from './fuel-efficiency/fuel-efficiency.component';


@NgModule({
  declarations: [
    TrackFuelConsumptionComponent,
    FuelRecordComponent,
    FuelEfficiencyComponent,
  ],
  imports: [CommonModule, FuelRecordRoutingModule],
  exports: [FuelRecordComponent],
})
export class FuelRecordModule {}
