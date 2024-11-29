import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { InsuranceManagementRoutingModule } from './insurance-management-routing.module';
import { InsuranceDetailsComponent } from './insurance-details/insurance-details.component';
import { InsuranceManagementComponent } from '../insurance-management/insurance-management.component';
import { InsuranceRenewalReminderComponent } from './insurance-renewal-reminder/insurance-renewal-reminder.component';
import { InsuranceClaimComponent } from './insurance-claim/insurance-claim.component';
import { InsuranceClaimTrackComponent } from './insurance-claim-track/insurance-claim-track.component';
import { SharedModule } from '../../shared/shared.module';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    InsuranceDetailsComponent,
    InsuranceManagementComponent,
    InsuranceRenewalReminderComponent,
    InsuranceClaimComponent,
    InsuranceClaimTrackComponent,
  ],

  imports: [
    CommonModule,
    InsuranceManagementRoutingModule,
    SharedModule,
  ],

  exports: [InsuranceManagementComponent],
})
export class InsuranceManagementModule {}
