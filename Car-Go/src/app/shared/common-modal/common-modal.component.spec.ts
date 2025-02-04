import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CommonModalComponent } from './common-modal.component';

describe('CommonComponent', () => {
  let component: CommonModalComponent;
  let fixture: ComponentFixture<CommonModalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [CommonModalComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(CommonModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
