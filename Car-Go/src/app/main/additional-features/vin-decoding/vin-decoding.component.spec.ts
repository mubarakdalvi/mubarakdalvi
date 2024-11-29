import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VinDecodingComponent } from './vin-decoding.component';

describe('VinDecodingComponent', () => {
  let component: VinDecodingComponent;
  let fixture: ComponentFixture<VinDecodingComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [VinDecodingComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(VinDecodingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
