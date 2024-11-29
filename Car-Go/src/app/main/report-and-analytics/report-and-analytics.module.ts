import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReportAndAnalyticsRoutingModule } from './report-and-analytics-routing.module';
import { ReportAndAnalyticsComponent } from '../report-and-analytics/report-and-analytics.component';
import { AnalyzeReportComponent } from './analyze-report/analyze-report.component';

@NgModule({
  declarations: [ReportAndAnalyticsComponent, AnalyzeReportComponent],
  imports: [CommonModule, ReportAndAnalyticsRoutingModule],
  exports: [ReportAndAnalyticsComponent],
})
export class ReportAndAnalyticsModule {}
