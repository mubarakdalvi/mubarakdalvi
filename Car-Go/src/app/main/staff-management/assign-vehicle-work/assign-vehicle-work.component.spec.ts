import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AssignVehicleWorkComponent } from './assign-vehicle-work.component';

describe('AssignVehicleWorkComponent', () => {
  let component: AssignVehicleWorkComponent;
  let fixture: ComponentFixture<AssignVehicleWorkComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [AssignVehicleWorkComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AssignVehicleWorkComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
