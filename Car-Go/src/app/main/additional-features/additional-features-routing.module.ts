import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AdditionalFeaturesComponent } from './additional-features.component';
import { VinDecodingComponent } from './vin-decoding/vin-decoding.component';

const routes: Routes = [
  {
    path: '',
    component: AdditionalFeaturesComponent,
    children: [{ path: 'vin-decoding', component: VinDecodingComponent }],
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class AdditionalFeaturesRoutingModule {}
