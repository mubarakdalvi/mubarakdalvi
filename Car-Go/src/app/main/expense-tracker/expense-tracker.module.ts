import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ExpenseTrackerRoutingModule } from './expense-tracker-routing.module';
import { ExpenseTrackerComponent } from './expense-tracker.component';
import { GenerateReportComponent } from './generate-report/generate-report.component';
import { RecordExpenseComponent } from './record-expense/record-expense.component';


@NgModule({
  declarations: [
    ExpenseTrackerComponent,
    GenerateReportComponent,
    RecordExpenseComponent,
  ],
  imports: [CommonModule, ExpenseTrackerRoutingModule],
  exports: [ExpenseTrackerComponent],
})
export class ExpenseTrackerModule {}
