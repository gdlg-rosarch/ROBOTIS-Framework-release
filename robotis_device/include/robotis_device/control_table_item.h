/*******************************************************************************
 * Copyright (c) 2016, ROBOTIS CO., LTD.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 * * Redistributions of source code must retain the above copyright notice, this
 *   list of conditions and the following disclaimer.
 *
 * * Redistributions in binary form must reproduce the above copyright notice,
 *   this list of conditions and the following disclaimer in the documentation
 *   and/or other materials provided with the distribution.
 *
 * * Neither the name of ROBOTIS nor the names of its
 *   contributors may be used to endorse or promote products derived from
 *   this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
 * OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *******************************************************************************/

/*
 * control_table_item.h
 *
 *  Created on: 2015. 12. 16.
 *      Author: zerom
 */

#ifndef ROBOTIS_DEVICE_CONTROL_TABLE_ITEM_H_
#define ROBOTIS_DEVICE_CONTROL_TABLE_ITEM_H_


#include <stdint.h>

namespace robotis_framework
{

enum AccessType {
  Read,
  ReadWrite
};

enum MemoryType {
  EEPROM,
  RAM
};

class ControlTableItem
{
public:
  std::string item_name_;
  uint16_t    address_;
  AccessType  access_type_;
  MemoryType  memory_type_;
  uint8_t     data_length_;
  int32_t     data_min_value_;
  int32_t     data_max_value_;
  bool        is_signed_;

  ControlTableItem()
    : item_name_(""),
      address_(0),
      access_type_(Read),
      memory_type_(RAM),
      data_length_(0),
      data_min_value_(0),
      data_max_value_(0),
      is_signed_(false)
  { }
};

}


#endif /* ROBOTIS_DEVICE_CONTROL_TABLE_ITEM_H_ */
