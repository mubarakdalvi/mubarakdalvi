import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MonitorPerformanceComponent } from './monitor-performance.component';

describe('MonitorPerformanceComponent', () => {
  let component: MonitorPerformanceComponent;
  let fixture: ComponentFixture<MonitorPerformanceComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [MonitorPerformanceComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MonitorPerformanceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
