import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ServiceRecordRoutingModule } from './service-record-routing.module';
import { ServiceHistoryComponent } from './service-history/service-history.component';
import { ServiceRecordComponent } from '../service-record/service-record.component';
import { ServiceInvoiceComponent } from './service-invoice/service-invoice.component';
import { ServiceRecieptComponent } from './service-reciept/service-reciept.component';

@NgModule({
  declarations: [
    ServiceRecordComponent,
    ServiceHistoryComponent,
    ServiceInvoiceComponent,
    ServiceRecieptComponent,
  ],
  imports: [CommonModule, ServiceRecordRoutingModule],
  exports: [ServiceRecordComponent],
})
export class ServiceRecordModule {}
