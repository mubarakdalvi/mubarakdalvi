import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { CoreRoutingModule } from './core-routing.module';
import { CoreComponent } from '../core/core.component';


@NgModule({
  declarations: [CoreComponent,],
  imports: [CommonModule, CoreRoutingModule],
  exports: [CoreComponent],
})
export class CoreModule {}
