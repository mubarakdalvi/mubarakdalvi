import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TrackFuelConsumptionComponent } from './track-fuel-consumption.component';

describe('TrackFuelConsumptionComponent', () => {
  let component: TrackFuelConsumptionComponent;
  let fixture: ComponentFixture<TrackFuelConsumptionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [TrackFuelConsumptionComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TrackFuelConsumptionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
