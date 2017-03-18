// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: main/resources/chat.proto

package com.talent.aio.examples.im.common.packets;

public interface BeginToLiveRespBodyOrBuilder extends
    // @@protoc_insertion_point(interface_extends:com.talent.aio.examples.im.common.packets.BeginToLiveRespBody)
    com.google.protobuf.MessageOrBuilder {

  /**
   * <pre>
   *消息发送时间
   * </pre>
   *
   * <code>int64 time = 1;</code>
   */
  long getTime();

  /**
   * <pre>
   *本次直播id
   * </pre>
   *
   * <code>int64 liveid = 2;</code>
   */
  long getLiveid();

  /**
   * <pre>
   *rtmp推流地址
   * </pre>
   *
   * <code>string rtmppublishurl = 3;</code>
   */
  java.lang.String getRtmppublishurl();
  /**
   * <pre>
   *rtmp推流地址
   * </pre>
   *
   * <code>string rtmppublishurl = 3;</code>
   */
  com.google.protobuf.ByteString
      getRtmppublishurlBytes();

  /**
   * <pre>
   *rtmp播放地址
   * </pre>
   *
   * <code>string rtmpliveurl = 4;</code>
   */
  java.lang.String getRtmpliveurl();
  /**
   * <pre>
   *rtmp播放地址
   * </pre>
   *
   * <code>string rtmpliveurl = 4;</code>
   */
  com.google.protobuf.ByteString
      getRtmpliveurlBytes();
}
