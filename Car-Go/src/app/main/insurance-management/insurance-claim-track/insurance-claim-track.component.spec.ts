import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InsuranceClaimTrackComponent } from './insurance-claim-track.component';

describe('InsuranceClaimTrackComponent', () => {
  let component: InsuranceClaimTrackComponent;
  let fixture: ComponentFixture<InsuranceClaimTrackComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [InsuranceClaimTrackComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(InsuranceClaimTrackComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
