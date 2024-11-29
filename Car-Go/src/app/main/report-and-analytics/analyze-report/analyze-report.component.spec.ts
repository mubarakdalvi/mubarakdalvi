import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AnalyzeReportComponent } from './analyze-report.component';

describe('AnalyzeReportComponent', () => {
  let component: AnalyzeReportComponent;
  let fixture: ComponentFixture<AnalyzeReportComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [AnalyzeReportComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AnalyzeReportComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
