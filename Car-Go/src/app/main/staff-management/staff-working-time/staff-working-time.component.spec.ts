import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StaffWorkingTimeComponent } from './staff-working-time.component';

describe('StaffWorkingTimeComponent', () => {
  let component: StaffWorkingTimeComponent;
  let fixture: ComponentFixture<StaffWorkingTimeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [StaffWorkingTimeComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(StaffWorkingTimeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
