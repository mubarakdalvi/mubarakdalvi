import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AdditionalFeaturesRoutingModule } from './additional-features-routing.module';
import { AdditionalFeaturesComponent } from '../additional-features/additional-features.component';
import { VinDecodingComponent } from '../additional-features/vin-decoding/vin-decoding.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [AdditionalFeaturesComponent, VinDecodingComponent],
  imports: [
    CommonModule,
    AdditionalFeaturesRoutingModule,
    ReactiveFormsModule,
    FormsModule,
  ],
  exports: [AdditionalFeaturesComponent],
})
export class AdditionalFeaturesModule {}
