import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MaintenanceReminderComponent } from './maintenance-reminder.component';

describe('MaintenanceReminderComponent', () => {
  let component: MaintenanceReminderComponent;
  let fixture: ComponentFixture<MaintenanceReminderComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [MaintenanceReminderComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MaintenanceReminderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
