import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { VehicleManagementRoutingModule } from './vehicle-management-routing.module';
import { VehicleManagementComponent } from './vehicle-management.component';
import { ManageVehicleComponent } from '../vehicle-management/manage-vehicle/manage-vehicle.component';
import { VehicleDetailsComponent } from './vehicle-details/vehicle-details.component';
import { UploadVehiclePhotoComponent } from './upload-vehicle-photo/upload-vehicle-photo.component';


@NgModule({
  declarations: [
    VehicleManagementComponent,
    ManageVehicleComponent,
    VehicleDetailsComponent,
    UploadVehiclePhotoComponent,
  ],
  imports: [CommonModule, VehicleManagementRoutingModule],
  exports: [VehicleManagementComponent],
})
export class VehicleManagementModule {}
