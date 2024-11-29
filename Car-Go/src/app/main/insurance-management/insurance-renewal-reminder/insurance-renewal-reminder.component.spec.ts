import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InsuranceRenewalReminderComponent } from './insurance-renewal-reminder.component';

describe('InsuranceRenewalReminderComponent', () => {
  let component: InsuranceRenewalReminderComponent;
  let fixture: ComponentFixture<InsuranceRenewalReminderComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [InsuranceRenewalReminderComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(InsuranceRenewalReminderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
