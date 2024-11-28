import { TestBed } from '@angular/core/testing';

import { WomensclothesService } from './womensclothes.service';

describe('WomensclothesService', () => {
  let service: WomensclothesService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(WomensclothesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
