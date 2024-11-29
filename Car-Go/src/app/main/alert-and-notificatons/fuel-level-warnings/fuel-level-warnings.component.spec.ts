import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FuelLevelWarningsComponent } from './fuel-level-warnings.component';

describe('FuelLevelWarningsComponent', () => {
  let component: FuelLevelWarningsComponent;
  let fixture: ComponentFixture<FuelLevelWarningsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [FuelLevelWarningsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FuelLevelWarningsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
